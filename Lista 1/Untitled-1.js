class Bigga{
    constructor(){
        this.state = 'quer maconha';
        this.haveWeed = true;
        this.weed = 10;
    }

    buyWeed(amount){
        this.weed += amount
    }

    bongada(){
        if (this.weed > 0){
            Weed.acende()
            Weed.puxa()
            Weed.prende()
            Weed.passa()
            this.weed --
            this.changeState('high')
        } else {
            alert('Desculpe, acabou a maconha')
            this.haveWeed = false
            this.changeState('triste')
            this.buyWeed(10)
        }
    }
    
    changeState(newState){
        this.state = newState
    }
}


export default function smokeWeed(){
    let Bigga = new Bigga()

    while (Bigga.haveWeed == true) {
        alert('Vocês se importam?');
        let resposta = Document.getElemntById('resposta');

        if (resposta == 'não'){
            Bigga.speak('top')
            Bigga.bongada()

        } else if (resposta == 'sim'){
            alert('se fuder meu')
            Bigga.changeState('triste')

        } else{
            Bigga.bongada()
        }
    }
}