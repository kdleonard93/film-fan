<script lang="ts">
  import { type Film, FilmStore } from "../../../film-store";
  import { onMount } from "svelte";

  export let data;
  let film: Film | null = null;

  // Reactive statement to fetch film details when 'data.id' changes
  $: if (data && data.id) {
    fetchFilmDetails();
  }

  async function fetchFilmDetails() {
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
  }
  onMount(fetchFilmDetails);
</script>

<div class="flex flex-col md:flex-row md:items-start overflow-hidden">
  {#if film}
    <div class="md:w-1/2">
      <img src={film.image} alt="Film" class="film-image" />
    </div>
    <div class="p-4 md:w-1/2">
      <h2 class="text-2xl font-bold mb-2">{film.name}</h2>
      <p class="mb-2">
        <span class="font-semibold">Directed by:</span> <i>{film.director}</i>
      </p>
      <p class="mb-2">{film.description}</p>
    </div>
  {:else}
    <div class="p-4">
      <p class="text-secondary-700">No film was found with ID {data.id}</p>
    </div>
  {/if}
</div>
