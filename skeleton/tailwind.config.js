/** @type {import('tailwindcss').Config} */
module.exports = {
	daisyui: {
		themes: [
			{
				custom: {
					"primary": '#facc15',
					"secondary": '#fb7185',
					"accent": '#a78bfa',
					"neutral": '#3D4451',
					"base-100" : '#FFFFFF',
					"info": '#3ABFF8',
					"success": '#36D399',
					"warning": '#fbbf24',
					"error": '#f87171',
				},
			},
		],
	},
	content: ['./templates/**/*.html', './static/src/**/*.js'],
	theme: {
		extend: {},
	},
	plugins: [require('daisyui')],
}
