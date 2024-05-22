import { writable } from "svelte/store";

export interface Film {
  id: number;
  name: string;
  director: string;
  description: string;
  release_year: number | null; // Using release_year to match your JSON and model
  image: string;
  tags: string[];
}

export const FilmStore = writable<Film[]>([]);
