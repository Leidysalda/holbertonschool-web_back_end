import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  get currency() {
    return this._currency;
  }

  set amount(amount) {
    if (typeof amount !== 'number') throw new Error('Amount must be a number');
    this._amount = amount;
  }

  set currency(currency) {
    if (!(currency instanceof Currency)) throw new Error('Currency must be a currency class');
    this._currency = currency;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  static convertPrice(amount, converionRate) {
    if (typeof amount !== 'number') throw new Error('Amount must be a number');
    if (typeof converionRate !== 'number') throw new Error('Conversion Rate must be a number');
    return amount * converionRate;
  }
}
