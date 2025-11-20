import { deLocalizeUrl } from '$lib/i18n/runtime';
import type { Reroute, Transport } from '@sveltejs/kit';
import { DateTime } from 'luxon';

export const reroute: Reroute = (request) => {
  return deLocalizeUrl(request.url).pathname;
};

export const transport: Transport = {
  DateTime: {
    encode: (value) => {
      return value instanceof DateTime && value.toObject();
    },
    decode: (value) => DateTime.fromObject(value),
  },
};
