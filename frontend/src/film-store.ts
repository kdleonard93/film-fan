import { writable } from 'svelte/store';
	
export const FilmStore = writable([
    { id: 1, name: "American Gangsta", releaseYear: 2007, director: "Ridley Scott" },
    { id: 2, name: "Fritz the Cat", releaseYear: 1972, director: "	Ralph Bakshi" },
])