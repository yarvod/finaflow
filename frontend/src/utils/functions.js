import moment from "moment";

export function isObject (value) {
    return value && typeof value === 'object' && value.constructor === Object;
}
export function parseURL (search) {
    const cut = search.split('?')
    if (cut.length === 2) {
        return JSON.parse('{"' + cut[1].replace(/&/g, '","').replace(/=/g,'":"') + '"}', function(key, value) { return key===""?value:decodeURIComponent(value) })
    }
}

export function checkEmail(email) {
    return email.match(/^(?=.{1,254}$)(?=.{1,64}@)[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/);
}

export function moneyFilter(value) {
    if (value) {
        return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, '.')
    }
}

moment.locale('ru')
export function dateFilter(value) {
  if (value) {
    return moment(String(value)).format('D MMM YYYY')
  }
}

export var groupBy = function(xs, key) {
  return xs.reduce(function(rv, x) {
    (rv[x[key]] = rv[x[key]] || []).push(x);
    return rv;
  }, {});
};

export function getMonthName(monthNumber) {
  const date = new Date();
  date.setMonth(monthNumber - 1);

  return date.toLocaleString('ru-RU', {
    month: 'long',
  });
}