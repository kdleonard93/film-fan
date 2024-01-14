<script lang="ts">
  export let data;
  import { goto } from "$app/navigation";
  import { FilmStore } from "../../film-store";
  import { onMount } from "svelte";

  onMount(async function () {
    if (!$FilmStore.length) {
      const endpoint = "http://localhost:8000/api/films/";
      const response = await fetch(endpoint);
      const data = await response.json();
      FilmStore.set(data);
    }
  });

  // let handleClick = () => {
  //   goto("/films/add/");
  // };
</script>

<div class="flex justify-center my-4">
  <div class="flex flex-wrap justify-center -mx-4">
    {#each $FilmStore as film}
      <div class="px-4 mb-4">
        <div
          class="border-r border-b border-l border-gray-400 lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal"
        >
          <img
            class="film-image"
            src={film.image}
            alt="Film"
            title="Card Image"
          />
          <div class="px-6 py-4">
            <div class="font-bold text-xl mb-2 text-secondary-700">
              {film.name}
            </div>
            <p class="text-secondary-700 text-base">
              Director: {film.director}
            </p>
            <p class="text-secondary-700 text-base">
              Release Year: {film.release_year}
            </p>
          </div>
          <div class="px-6 pt-4 pb-2">
            <a
              class="btn variant-filled-primary p-2 m-3 font-semibold"
              href="films/{film.id}">Details</a
            >
          </div>
        </div>
      </div>
    {/each}
  </div>
</div>
