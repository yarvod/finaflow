const VUE_APP_YANDEX_OAUTH2_CLIENT_ID = 'dd299b1fea2c4aebb1f90675e1e560ef';
const VUE_APP_YANDEX_OAUTH2_REDIRECT = 'https://finaflow.ru/login/yandex';
export const getYandexUrl = (from) => {
  const rootUrl = `https://oauth.yandex.ru/authorize?`;

  const options = {
    redirect_uri: VUE_APP_YANDEX_OAUTH2_REDIRECT,
    client_id: VUE_APP_YANDEX_OAUTH2_CLIENT_ID,
    response_type: 'code',
    force_confirm: true,
    state: from,
  };

  const qs = new URLSearchParams(options);

  return `${rootUrl}?${qs.toString()}`;
};