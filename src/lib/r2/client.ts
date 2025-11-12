import { env } from '$env/dynamic/private';
import S3mini from 's3mini';

export function getR2() {
  return new S3mini({
    accessKeyId: env.R2_ACCESS_KEY_ID ?? '',
    secretAccessKey: env.R2_SECRET_ACCESS_KEY ?? '',
    endpoint: env.R2_ENDPOINT ?? '',
  });
}
