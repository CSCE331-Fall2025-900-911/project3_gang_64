<script lang="ts">
  import { page } from '$app/state';
  import logo from '$lib/assets/logo.png';
  import { Card, CardBody, CardHeader, CardTitle } from '@immich/ui';
  console.log(page.url.hash.replace('#', ''));
  const error = page.url.searchParams.get('error');

  let errorMessage = 'An unknown error occurred.';
  let errorTitle = 'Sign-In Failed';

  if (error === 'AccessDenied') {
    errorTitle = 'Access Denied';
    errorMessage =
      'Sign-in failed. This application is for authorized employees only. Please contact support if you believe this is an error.';
  } else if (error) {
    // A catch-all for other auth errors
    errorMessage = `An error occurred during authentication. Code: ${error}`;
  }
</script>

<div class="flex justify-center">
  <div class="align-center mx-5 my-3 size-fit bg-black">
    <img class="my-10 w-100" src={logo} alt="Share Tea" />
    <Card>
      <CardHeader>
        <CardTitle>{errorTitle}</CardTitle>
      </CardHeader>
      <CardBody>
        {errorMessage}
      </CardBody>
    </Card>
  </div>
</div>
