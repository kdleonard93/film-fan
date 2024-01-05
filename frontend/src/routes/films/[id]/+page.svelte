<script lang="ts">
  import type { PageData } from "./$types";
  import { FilmStore } from "../../../film-store";

  export let data: PageData;
  let film = $FilmStore.find((film) => film.id == Number(data.id));
  console.log(film);
</script>

{#if film}
  <p>
    {film.name}, directed by: {film.director}. Released in {film.releaseYear}
  </p>
{:else}
  <p>No film was fond with ID {data.id}</p>
{/if}
