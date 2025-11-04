<script lang="ts">
  import { page } from '$app/state';
  import google from '$lib/assets/google.png';
  import logo from '$lib/assets/logo.png';
  import { Button, Card, CardBody, CardHeader, CardTitle } from '@immich/ui';
  console.log(page.url.hash.replace('#', ''));
</script>

<div class="flex justify-center">
  <div class="align-center mx-5 my-3 size-fit bg-black">
    <img class="my-10 w-100" src={logo} alt="Share Tea" />
    <Card>
      <CardHeader>
        <CardTitle>Login to Sharetea:</CardTitle>
      </CardHeader>
      <CardBody>
        <Button class="h-25 justify-self-center">
          <img class="h-20" src={google} alt="google logo" />
          Continue with Google
        </Button>
      </CardBody>
    </Card>
  </div>
</div>
