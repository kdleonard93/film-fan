<script lang="ts">
  export let data;

  import { FilmStore } from "../../film-store";
</script>

<ul>
  {#each $FilmStore as film}
    <li>
      <a href="films/{film.id}">{film.name}</a>
    </li>
  {/each}
</ul>

<button type="button" class="btn variant-filled-primary p-2 m-2 font-semibold"
  >Add Film</button
>
