<script lang="ts">
  import logo from '$lib/assets/logo.png';
  import { Button, Card, CardBody, CardHeader, CardTitle, Stack } from '@immich/ui';
  import { mdiSilverware, mdiTablet } from '@mdi/js';
  import { localizeHref } from '$lib/i18n/runtime';
</script>

<div class="flex justify-center">
  <div class="align-center mx-5 my-3 size-fit">
    <img class="mx-auto my-10 w-100" src={logo} alt="Share Tea" />
    <Card>
      <CardHeader>
        <CardTitle>Interface Portal</CardTitle>
      </CardHeader>
      <CardBody>
        <Stack>
          <Button leadingIcon={mdiSilverware} href={localizeHref('/kitchen')}>Kitchen Interface</Button>
          <Button leadingIcon={mdiTablet} href={localizeHref('/kiosk')}>Kiosk Interface</Button>
        </Stack>
      </CardBody>
    </Card>
  </div>
</div>
