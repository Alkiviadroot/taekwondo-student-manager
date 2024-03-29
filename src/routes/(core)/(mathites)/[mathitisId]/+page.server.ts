import { redirect, fail } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms/server';
import { mathitis, provlimata, deltia, exetasi, timi,pliromeS } from '$lib/schemas';
import moment from 'moment';

let provlimataNotAvailable = false;
let provlimataId: string;
let deltiaNotAvailable = false;
let deltiId: string;
let programa: any = [];

export const load = async ({ locals, params }: any) => {
	const mathitisId = params.mathitisId;
	// MathitisForm
	let profile: any = [];
	try {
		profile = await locals.pb.collection('mathites').getOne(mathitisId);
	} catch {
		throw redirect(307, '/');
	}

	if (profile.tk == 0) profile.tk = undefined;
	if (profile.kinito == 0) profile.kinito = undefined;
	if (profile.tilefonoS == 0) profile.tilefonoS = undefined;
	if (profile.tilefonoE == 0) profile.tilefonoE = undefined;
	if (profile.email == '') profile.email = undefined;
	if (profile.fotografia == '') profile.fotografia = undefined;
	profile.genethliaRaw = profile.genethlia;
	profile.enarksiRaw = profile.enarksi;
	profile.genethlia = moment(profile.genethlia).format('YYYY-MM-DD');
	profile.enarksi = moment(profile.enarksi).format('YYYY-MM-DD');


	const mathitisForm = await superValidate(profile, mathitis);

	// ProvlimataForm
	let provlimataR: any = [];
	try {
		provlimataR = await locals.pb.collection('provlimata').getFirstListItem('mathitis="' + mathitisId + '"');
		provlimataId = provlimataR.id;
		provlimataNotAvailable = false;
	} catch {
		provlimataNotAvailable = true;
	}
	const provlimataForm = await superValidate(provlimataR, provlimata);

	// DeltiaForm
	let deltiaR: any = [];
	try {
		deltiaR = await locals.pb.collection('deltia').getFirstListItem('mathitis="' + mathitisId + '"');

		deltiId = deltiaR.id;
		deltiaNotAvailable = false;
		if (deltiaR.gal_Number == 0) deltiaR.gal_Number = undefined;
		if (deltiaR.forma_GDPR == '') deltiaR.forma_GDPR = undefined;
		deltiaR.deltio_IgiasRaw = deltiaR.deltio_Igias;
		deltiaR.gal_DateRaw = deltiaR.gal_Date;
		deltiaR.deltio_Igias = moment(deltiaR.deltio_Igias).format('YYYY-MM-DD');
		deltiaR.gal_Date = moment(deltiaR.gal_Date).format('YYYY-MM-DD');

	} catch {
		deltiaNotAvailable = true;
	}

	const deltiaForm = await superValidate(deltiaR, deltia);

	let epafes: any = [];
	try {
		epafes = await locals.pb.collection('epafes').getFullList({
			filter: 'mathitis = "' + mathitisId + '"',
			sort: '-paralavi'
		});

	} catch {
		console.log('no record');
	}

	let exetasis: any = [];
	try {
		exetasis = await locals.pb.collection('eksetasis').getFullList({
			filter: 'mathitis = "' + mathitisId + '"'
		});

	} catch {
		console.log('no record');
	}

	const exetasiForm = await superValidate(exetasi);

	let exetasiCounter = 0;
	for (const exetasi of exetasis) {
		if (exetasi.epitixia) {
			exetasiCounter += 1;
			exetasi.zoni = exetasiCounter;
		} else {
			exetasi.zoni = exetasiCounter + 1;
		}
	}

	const zoni = exetasiCounter;

	const meresAll = await locals.pb.collection('meres').getFullList({
		sort: 'sort'
	})


	try {
		programa = await locals.pb.collection('programa').getFullList({
			filter: 'mathitis = "' + mathitisId + '"'
		});
	} catch {
		console.log('no record');
	}

	const meresMathiti = [];
	for (const mera of meresAll) {
		for (const p of programa) {
			if (mera.id == p.mera) {
				meresMathiti.push(mera);
				break;
			}
		}
	}

	let parousies: any = [];
	try {
		parousies = await locals.pb.collection('parousies').getFullList({
			filter: 'mathitis = "' + mathitisId + '"'
		});

	} catch {
		console.log('no record');
	}

	let pliromes: any = [];
	try {
		pliromes = await locals.pb.collection('pliromes').getFullList({
			filter: 'mathitis = "' + mathitisId + '"'
		});

	} catch {
		console.log('no record');
	}

	let parousiesTable: any = [];

	for (const parousia of parousies) {
		let exist = false;
		const id = parousia.xronos.toString() + parousia.minas.toString()
		let data = {
			id: id,
			minas: parousia.minas,
			xronos: parousia.xronos,
			parousies: 1,
			pliromenos: false,
			timi: 0
		}
		if (parousiesTable.length == 0) {
			parousiesTable.push(data);
		} else {
			for (const row of parousiesTable) {

				if (row.id == id) {
					row.parousies = row.parousies + 1;
					exist = true;
					break;
				}
			}
			if (!exist) parousiesTable.push(data);
		}

		for (const row of parousiesTable) {
			for (const pliromenos of pliromes) {
				const id = pliromenos.xronos.toString() + pliromenos.minas.toString()
				if (row.id == id) {
					row.pliromenos = true;
					row.timi = pliromenos.timi
					break;
				}
			}
		}
	}
	// sort
	parousiesTable.sort((a: any, b: any) => {
		const idA = a.id;
		const idB = b.id;
		// Use localeCompare to compare strings numerically
		return idA.localeCompare(idB);
	});

	const uniqueXronosSet = new Set();
	parousiesTable.forEach((obj: any) => {
		uniqueXronosSet.add(obj.xronos);
	});

	// Convert the Set back to an array to get the unique 'xronos' values
	const uniqueXronosArray = Array.from(uniqueXronosSet).reverse();

	const pliromiForm = await superValidate(pliromeS);

	return {
		profile,
		mathitisForm,
		provlimataForm,
		provlimataR,
		deltiaForm,
		deltiaR,
		epafes,
		zoni,
		exetasiForm,
		exetasis,
		programa,
		meresAll,
		meresMathiti,
		parousiesTable,
		uniqueXronosArray,
		pliromiForm
	};
};

export const actions = {
	mathitis: async ({ request, locals, params }: any) => {
		const form = await request.formData();
		const mathitisForm = await superValidate(form, mathitis);

		if (!mathitisForm.valid) {
			return fail(400, {
				mathitisForm
			});
		}

		const formData = new FormData();
		//Required
		formData.append('id', params.mathitisId);
		formData.append('onoma', mathitisForm.data.onoma);
		formData.append('epitheto', mathitisForm.data.epitheto);
		formData.append('energos', mathitisForm.data.energos);
		//Opional
		formData.append(
			'diefthinsi',
			mathitisForm.data.diefthinsi !== undefined ? mathitisForm.data.diefthinsi : ''
		);
		formData.append(
			'tk',
			mathitisForm.data.tk !== undefined ? mathitisForm.data.tk.toString() : ''
		);
		formData.append(
			'perioxi',
			mathitisForm.data.perioxi !== undefined ? mathitisForm.data.perioxi : ''
		);
		formData.append(
			'kinito',
			mathitisForm.data.kinito !== undefined ? mathitisForm.data.kinito.toString() : ''
		);
		formData.append(
			'tilefonoS',
			mathitisForm.data.tilefonoS !== undefined ? mathitisForm.data.tilefonoS.toString() : ''
		);
		formData.append(
			'tilefonoE',
			mathitisForm.data.tilefonoE !== undefined ? mathitisForm.data.tilefonoE.toString() : ''
		);
		formData.append(
			'epankelma',
			mathitisForm.data.epankelma !== undefined ? mathitisForm.data.epankelma : ''
		);
		formData.append(
			'genethlia',
			mathitisForm.data.genethlia !== undefined ? mathitisForm.data.genethlia : ''
		);
		formData.append(
			'enarksi',
			mathitisForm.data.enarksi !== undefined ? mathitisForm.data.enarksi : ''
		);
		formData.append('email', mathitisForm.data.email !== undefined ? mathitisForm.data.email : '');

		const file = form.get('fotografia');
		if (file instanceof File && file?.size != 0) {
			const name =
				mathitisForm.data.onoma.toString() +
				'_' +
				mathitisForm.data.epitheto.toString() +
				'.' +
				file.type.replace('image/', '');
			formData.append('fotografia', new Blob([file]), name);
		}

		await locals.pb.collection('mathites').update(params.mathitisId, formData);
	},

	mathitisDelete: async ({ locals, params }: any) => {
		await locals.pb.collection('mathites').delete(params.mathitisId);
		throw redirect(303, '/');
	},

	provlimata: async ({ request, locals, params }: any) => {
		const form = await request.formData();
		const provlimataForm = await superValidate(form, provlimata);

		if (!provlimataForm.valid) {
			return fail(400, {
				provlimataForm
			});
		}

		provlimataForm.data.mathitis = params.mathitisId;
		if (provlimataForm.data.kardiaka == 'false') provlimataForm.data.kardiakaL = '';
		if (provlimataForm.data.asthma == 'false') provlimataForm.data.asthmaL = '';
		if (provlimataForm.data.lipothimia == 'false') provlimataForm.data.lipothimiaL = '';
		if (provlimataForm.data.allo == 'false') provlimataForm.data.alloL = '';

		if (provlimataNotAvailable)
			await locals.pb.collection('provlimata').create(provlimataForm.data);
		else await locals.pb.collection('provlimata').update(provlimataId, provlimataForm.data);
	},

	deltia: async ({ request, locals, params }: any) => {
		const form = await request.formData();
		const deltiaForm = await superValidate(form, deltia);

		if (!deltiaForm.valid) {
			return fail(400, {
				deltiaForm
			});
		}

		const formData = new FormData();
		//Required
		formData.append('mathitis', params.mathitisId);
		formData.append('fotografia_adia', deltiaForm.data.fotografia_adia);
		//Opional
		formData.append(
			'gal_Number',
			deltiaForm.data.gal_Number !== undefined ? deltiaForm.data.gal_Number.toString() : ''
		);
		formData.append(
			'gal_Date',
			deltiaForm.data.gal_Date !== undefined ? deltiaForm.data.gal_Date : ''
		);
		formData.append(
			'deltio_Igias',
			deltiaForm.data.deltio_Igias !== undefined ? deltiaForm.data.deltio_Igias : ''
		);

		const file = form.get('forma_GDPR');
		if (file instanceof File && file?.size != 0) {
			const name = params.mathitisId + '.' + file.type.replace('image/', '');
			formData.append('forma_GDPR', new Blob([file]), name);
		}

		if (deltiaNotAvailable) await locals.pb.collection('deltia').create(formData);
		else await locals.pb.collection('deltia').update(deltiId, formData);
	},

	exetasi: async ({ request, locals, params }: any) => {
		const form = await request.formData();
		const exetasiForm = await superValidate(form, exetasi);

		if (!exetasiForm.valid) {
			return fail(400, {
				exetasiForm
			});
		}

		exetasiForm.data.mathitis = params.mathitisId;
		await locals.pb.collection('eksetasis').create(exetasiForm.data);
	},

	programaSave: async ({ request, locals, params }: any) => {
		const form = await request.formData();
		const meres = form.get('progrmaMeres') as string;
		const obj = JSON.parse(meres);

		for (const p of programa) {
			try {
				await locals.pb.collection('programa').delete(p.id);
			} catch { }
		}
		for (const meres of obj) {
			try {
				const formData = new FormData();
				formData.append('mathitis', params.mathitisId);
				formData.append('mera', meres);
				await locals.pb.collection('programa').create(formData);
			} catch { }
		}
	},
	pliromi: async ({ request, locals, params }: any) => {
		const form = await request.formData();
		const pliromiForm = await superValidate(form, pliromeS);
		if (!pliromiForm.valid) {
			return fail(400, {
				pliromiForm
			});
		}

		pliromiForm.data.mathitis = params.mathitisId;
		await locals.pb.collection('pliromes').create(pliromiForm.data);
	}
};
