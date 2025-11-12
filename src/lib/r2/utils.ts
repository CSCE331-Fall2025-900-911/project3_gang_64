import { uploadImageToR2 } from '$lib/api/r2.remote';

export function fileToBase64(file: File): Promise<string> {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(reader.result as string);
    reader.onerror = (error) => reject(error);
    reader.readAsDataURL(file);
  });
}

export function fileUpload(): Promise<string> {
  return new Promise((resolve, reject) => {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = '.png, .jpg, .jpeg';
    input.onchange = async (e) => {
      const files = (e.target as HTMLInputElement).files;
      if (files && files.length > 0) {
        console.log('Selected file:', files[0]);

        const upload = await uploadImageToR2({
          file: await fileToBase64(files[0]),
          extension: files[0].type.split('/')[1],
        });

        if (!upload.key) {
          return reject('Upload failed');
        }

        resolve(upload.key);
      }
    };

    input.click();
  });
}
