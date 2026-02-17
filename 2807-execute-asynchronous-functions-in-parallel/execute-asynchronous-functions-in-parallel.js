var promiseAll = function(functions) {
  return new Promise((resolve, reject) => {
    if (functions.length === 0) {
      resolve([]);
      return;
    }

    const results = new Array(functions.length);
    let done = 0;

    functions.forEach((fn, i) => {
      try {
        fn().then(val => {
          results[i] = val;
          done++;
          if (done === functions.length) resolve(results);
        }).catch(reject);
      } catch (e) {
        reject(e);
      }
    });
  });
};
