var cancellable = function(fn, args, t) {
  fn(...args);
  const id = setInterval(() => fn(...args), t);
  return function cancelFn() {
    clearInterval(id);
  };
};
