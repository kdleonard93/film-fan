<script lang="ts">
  import "../app.postcss";
  import { page } from "$app/stores";
  import { TabGroup, Tab, TabAnchor } from "@skeletonlabs/skeleton";
</script>

<TabGroup justify="justify-center">
  <TabAnchor href="/" selected={$page.url.pathname === "/"}>Home</TabAnchor>
  <TabAnchor href="/films" selected={$page.url.pathname === "/films"}
    >Films</TabAnchor
  >
  <TabAnchor href="/films/add" selected={$page.url.pathname === "/films/add/"}
    >Add New Film</TabAnchor
  >
</TabGroup>

<slot />
