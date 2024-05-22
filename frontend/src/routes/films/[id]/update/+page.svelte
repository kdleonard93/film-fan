<script lang="ts">
  export let data;
  import { goto } from "$app/navigation";
  import { type Film, FilmStore } from "../../../../film-store";
  import { FileButton } from "@skeletonlabs/skeleton";
  import { onMount } from "svelte";

  let name: string = "";
  let director: string = "";
  let release_year: string = "";
  let description: string = "";
  let imageFile: File | null = null;
  let film: Film | null = null;
  let id: number;
  let tags: string = "";

  // Reactive statement to fetch film details when 'data.id' changes
  $: if (data && data.id) {
    fetchFilmDetails();
  }

  const handleFileChange = (event: Event) => {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files[0]) {
      imageFile = input.files[0];
    }
  };

  let handleSubmit = () => {
    if (!film) {
      console.error("No film data available");
      return;
    }
    const endpoint = `http://localhost:8000/api/films/${id}/`;
    let data = new FormData();
    data.append("name", name);
    data.append("director", director);
    data.append("description", description);
    data.append("release_year", release_year);
    if (imageFile) {
      data.append("image", imageFile);
    }

    fetch(endpoint, { method: "PUT", body: data })
      .then((response) => response.json())
      .then((data) => {
        FilmStore.update((prev) => {
          let updatedFilms = $FilmStore.slice();
          let index = updatedFilms.findIndex((film) => film.id == data.id);
          updatedFilms[index] = data;
          return updatedFilms;
        });
      });

    goto("/films/");
  };
  async function fetchFilmDetails() {
    id = Number(data.id);
    if ($FilmStore.length) {
      const foundFilm = $FilmStore.find((f) => f.id == Number(data.id));
      film = foundFilm !== undefined ? foundFilm : null;
    } else {
      const endpoint = `http://localhost:8000/api/films/${data.id}/`;
      let response = await fetch(endpoint);
      if (response.status == 200) {
        film = await response.json();
      } else {
        film = null;
      }
    }
    if (film) {
      name = film.name || "";
      director = film.director || "";
      release_year = film.release_year ? film.release_year.toString() : "";
      description = film.description || "";
    }
  }
  onMount(fetchFilmDetails);
</script>

<div class="flex justify-center my-4">
  <form
    class="bg-slate shadow-md rounded px-8 pt-6 pb-8 mb-4"
    on:submit|preventDefault={handleSubmit}
  >
    <h3 class="font-semibold text-2xl sm:text-3xl md:text-4xl mb-2">
      Update Film
    </h3>
    <label class="label block font-bold mb-2">
      <span>Name</span>
      <input class="input" type="text" placeholder="name" bind:value={name} />
    </label>

    <label class="label block font-bold mb-2">
      <span>Director</span>
      <input
        class="input"
        type="text"
        placeholder="director"
        bind:value={director}
      />
    </label>

    <label class="label block font-bold mb-2">
      <span>Release Year</span>
      <input
        type="number"
        class="input"
        placeholder="Release Year"
        bind:value={release_year}
        min="1900"
        max={new Date().getFullYear()}
      />
    </label>

    <label class="label block font-bold mb-2">
      <span>Description</span>
      <textarea
        class="textarea"
        rows="4"
        placeholder="Film description..."
        bind:value={description}
      />
    </label>

    <label class="label block font-bold mb-2">
      <span>Image</span>
      <input class="file" type="file" on:change={handleFileChange} />
    </label>

    <button
      type="submit"
      class="btn variant-filled-primary p-2 m-3 font-semibold">Submit</button
    >
  </form>
</div>
