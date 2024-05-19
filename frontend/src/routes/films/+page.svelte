<script lang="ts">
  export let data;
  import { FilmStore } from "../../film-store";
  import { onMount } from "svelte";
  import { getModalStore } from "@skeletonlabs/skeleton";
  import type { ModalSettings } from "@skeletonlabs/skeleton";

  const modalStore = getModalStore();

  let tags = [];

  let setTags = () => {
    let tagSet = new Set();
    $FilmStore.map((film) => film.tags.forEach((tag) => tagSet.add(tag)));
    tags = Array.from(tagSet);
  };

  onMount(async function () {
    if (!$FilmStore.length) {
      const endpoint = "http://localhost:8000/api/films/";
      const response = await fetch(endpoint);
      const data = await response.json();
      FilmStore.set(data);
    }
    setTags();
  });

  let handleDelete = (id: number) => {
    const modal: ModalSettings = {
      type: "confirm",
      title: "Please Confirm",
      body: "Are you sure you want to delete this film?",
      response: (isConfirmed: boolean) => {
        if (isConfirmed) {
          const endpoint = `http://localhost:8000/api/films/${id}`;
          fetch(endpoint, { method: "DELETE" }).then((response) => {
            if (response.status == 204) {
              FilmStore.update((prev) => prev.filter((film) => film.id != id));
            }
          });
        }
      },
    };
    modalStore.trigger(modal);
  };
</script>

<div class="container h-full mx-auto flex justify-center items-center">
  <div class="space-y-5">
    <h2 class="mb-4 h2">Film List</h2>
  </div>
</div>

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
            <button
              class="btn variant-filled-error p-2 m-3 font-semibold"
              on:click={() => handleDelete(film.id)}>Delete</button
            >
          </div>
        </div>
      </div>
    {/each}
  </div>
</div>
