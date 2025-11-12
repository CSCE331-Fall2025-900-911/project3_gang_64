import { command } from '$app/server';
import { env } from '$env/dynamic/private';
import { getR2 } from '$lib/r2/client';
import * as v from 'valibot';

const uploadImageSchema = v.object({
  file: v.string(),
  extension: v.string(),
});

function base64ToFile(base64: string, ext: string): File {
  const mime = `application/${ext}`; // simple mime guess based on extension
  const byteString = atob(base64.split(',')[1] || base64);
  const ab = new ArrayBuffer(byteString.length);
  const ia = new Uint8Array(ab);

  for (let i = 0; i < byteString.length; i++) {
    ia[i] = byteString.charCodeAt(i);
  }

  return new File([ab], `file.${ext}`, { type: mime });
}

export const uploadImageToR2 = command(uploadImageSchema, async ({ file: base64, extension }) => {
  const r2 = getR2();

  const file = base64ToFile(base64, extension);
  const objectKey = crypto.randomUUID() + '.' + extension;

  // Convert File to ArrayBuffer
  const arrayBuffer = await file.arrayBuffer();
  const buffer = Buffer.from(arrayBuffer);

  await r2.putObject(objectKey, buffer);

  return {
    key: objectKey,
    url: `https://${env.R2_PUBLIC}/${objectKey}`,
  };
});
