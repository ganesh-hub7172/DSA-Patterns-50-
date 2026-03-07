class EventEmitter {
    constructor() {
        this.events = {};
    }

    subscribe(eventName, callback) {
        if (!this.events[eventName]) {
            this.events[eventName] = [];
        }

        this.events[eventName].push(callback);

        const callbacks = this.events[eventName];

        return {
            unsubscribe: () => {
                const index = callbacks.indexOf(callback);
                if (index !== -1) {
                    callbacks.splice(index, 1);
                }
            }
        };
    }

    emit(eventName, args = []) {
        if (!this.events[eventName]) return [];

        const results = [];

        for (const cb of this.events[eventName]) {
            results.push(cb(...args));
        }

        return results;
    }
}