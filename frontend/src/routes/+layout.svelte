<script lang="ts">
  export let y = 0;
  import "../app.postcss";
  import { page } from "$app/stores";
  import { TabGroup, Tab, TabAnchor } from "@skeletonlabs/skeleton";

  let tabs = [
    { name: "Home", link: "/" },
    { name: "Films", link: "/films" },
    { name: "Add New Film", link: "/films/add" },
  ];
</script>

<header
  class={"sticky z-[10] w-full top-0 duration-200 px-6 flex items-center justify-between " +
    (y > 0
      ? "py-4 bg-secondary-400 border border-slate-900"
      : "py-6 bg-transparent border-transparent")}
>
  <h1 class="font-medium">Fanflix 🎞️</h1>
  <TabGroup
    justify="justify-center"
    class="flex items-center gap-4 border-none"
  >
    {#each tabs as tab}
      <TabAnchor href={tab.link} selected={$page.url.pathname === tab.link}>
        {tab.name}
      </TabAnchor>
    {/each}
  </TabGroup>
</header>

<slot />
