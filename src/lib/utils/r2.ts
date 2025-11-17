import { env } from '$env/dynamic/public';
import { uploadImageToR2 } from '$lib/api/r2.remote';

export function fileToBase64(file: File): Promise<string> {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(reader.result as string);
    reader.onerror = (error) => reject(error);
    reader.readAsDataURL(file);
  });
}

export async function fileUpload(file: File): Promise<string> {
  const upload = await uploadImageToR2({
    file: await fileToBase64(file),
    extension: file.type.split('/')[1],
  });

  if (!upload.key) {
    throw new Error('Upload failed');
  }

  return `${env.PUBLIC_R2_ENDPOINT}/${upload.key}`;
}
