import { join } from 'path'
import type { Config } from 'tailwindcss'
import forms from '@tailwindcss/forms';
import { skeleton } from '@skeletonlabs/tw-plugin';
import { nineties } from './src/nineties'

export default {
	darkMode: 'class',
	content: ['./src/**/*.{html,js,svelte,ts}', join(require.resolve('@skeletonlabs/skeleton'), '../**/*.{html,js,svelte,ts}')],
	theme: {
		extend: {
			colors: {
				'hashnode-blue': '#2463EB',
				'cali-gold': '#FFC30B',
				'paddle-tan': '#93645F'
			}
		},
	},
	plugins: [
		forms,
		skeleton({
			themes: {
				preset: [
					{
						name: 'gold-nouveau',
						enhancements: true,
					},
					{
						name: 'vintage',
						enhancements: true,
					},
				],
				custom: [
					nineties,
				],
			},
		}),
	],
} satisfies Config;
