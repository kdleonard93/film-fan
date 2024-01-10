<script lang="ts">
  export let data;
  import { goto } from "$app/navigation";
  import { FilmStore } from "../../../film-store";

  let name = "";
  let director = "";
  let releaseYear = "";

  let handleSubmit = () => {
    FilmStore.update((films) => {
      let newId = films.length > 0 ? films[films.length - 1].id + 1 : 1;
      let newFilm = {
        id: newId,
        name: name,
        director: director,
        releaseYear: parseInt(releaseYear, 10) || null,
      };
      return [...films, newFilm];
    });
    goto("/films/");
  };
</script>

<div class="flex justify-center my-4">
  <form
    class="bg-slate shadow-md rounded px-8 pt-6 pb-8 mb-4"
    on:submit|preventDefault={handleSubmit}
  >
    <h3 class="font-semibold text-2xl sm:text-3xl md:text-4xl mb-2">
      Add New Film
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
        bind:value={releaseYear}
        min="1900"
        max={new Date().getFullYear()}
      />
    </label>

    <button
      type="submit"
      class="btn variant-filled-primary p-2 m-3 font-semibold">Submit</button
    >
  </form>
</div>
