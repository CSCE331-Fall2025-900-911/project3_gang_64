<script lang="ts">
  import { page } from '$app/state';
  import { Card, CardTitle, CardHeader , Button, CardBody} from '@immich/ui';
  import google from '$lib/assets/google.png' ;
  import logo from  '$lib/assets/logo.png'
  console.log(page.url.hash.replace('#', ''));
</script>

<div class="flex justify-center">
  <div class="bg-black align-center mx-5 my-3 size-fit">
    <img class = "w-100 my-10" src={logo}/>
  <Card >
    <CardHeader>
      <CardTitle>Login to Sharetea:</CardTitle>
    </CardHeader>
    <CardBody>
        <Button class = "h-25 justify-self-center">
          <img class = "h-20" src = {google} alt= "google logo" />
          Continue with Google
        </Button>
    </CardBody>
  </Card>
  </div>
</div>