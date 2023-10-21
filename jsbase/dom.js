class Circle{
    constructor(radius){
        this.radius = radius;
    }
    area(){
        return Math.PI*this.radius*this.radius;
    }
}

const Area = new Circle(12);
const areavalue = Area.area();
console.log(`area of thiis circle is ${areavalue}`);