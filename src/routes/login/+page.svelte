<script lang="ts">
  import { SignIn, SignOut } from '@auth/sveltekit/components';
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
        <SignIn>
          <div slot="submitButton" class="buttonPrimary">Sign in</div>
        </SignIn>
        <SignIn provider="google" />
      </CardBody>
    </Card>
  </div>
</div>
