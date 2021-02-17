interface Product {
    doStuff(): string;
}

class ConcreteProductA implements Product {
    doStuff(): string {
        return "ConcreteA!"
    }
}

class ConcreteProductB implements Product {
    doStuff(): string {
        return "ConcreteB!"
    }
}

class Creator {
    someOperation(): boolean {
        return true;
    }

    createProduct(): Product {
        throw new Error("not implemented");
    }
}

class ConcreteCreatorA extends Creator {
    createProduct(): Product {
        return new ConcreteProductA();
    }
}

class ConcreteCreatorB extends Creator {
    createProduct(): Product {
        return new ConcreteProductB();
    }
}