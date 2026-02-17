Function.prototype.callPolyfill = function(obj, ...args) {
  obj = obj ?? globalThis;
  const key = Symbol();
  obj[key] = this;
  const res = obj[key](...args);
  delete obj[key];
  return res;
};
