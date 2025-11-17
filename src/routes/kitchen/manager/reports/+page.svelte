<script>
  import { Card, CardBody, CardHeader, CardTitle, Heading, Text } from '@immich/ui';
  import { t } from '$lib/utils/utils';
</script>

<Heading size="large" class="mt-2 mb-6">{t('manager_reports_title')}</Heading>

<div class="mt-4 flex flex-col gap-4">
  <Card expandable>
    <CardHeader>
      <CardTitle>{t('manager_reports_x_title')}</CardTitle>
    </CardHeader>
    <CardBody>
      <Text>{t('manager_reports_x_info')}</Text>
    </CardBody>
  </Card>

  <Card expandable>
    <CardHeader>
      <CardTitle>{t('manager_reports_z_title')}</CardTitle>
    </CardHeader>
    <CardBody>
      <Text>{t('manager_reports_z_info')}</Text>
    </CardBody>
  </Card>
</div>
