const VUE_APP_GOOGLE_OAUTH2_CLIENT_ID = '868501099101-vl4gi2os8r2jp1qfmb7ickja1jr0p08d.apps.googleusercontent.com';
const VUE_APP_GOOGLE_OAUTH2_REDIRECT = 'https://finaflow.ru/login/google';
export const getGoogleUrl = (from) => {
  const rootUrl = `https://accounts.google.com/o/oauth2/v2/auth`;

  const options = {
    redirect_uri: VUE_APP_GOOGLE_OAUTH2_REDIRECT,
    client_id: VUE_APP_GOOGLE_OAUTH2_CLIENT_ID,
    access_type: 'offline',
    response_type: 'code',
    prompt: 'consent',
    scope: [
      'https://www.googleapis.com/auth/userinfo.profile',
      'https://www.googleapis.com/auth/userinfo.email',
    ].join(' '),
    state: from,
  };

  const qs = new URLSearchParams(options);

  return `${rootUrl}?${qs.toString()}`;
};