(function(window, $){

    var Dice = function(containerSelector){

        if( Dice.prototype._singletonInstance ) {
            return Dice.prototype._singletonInstance;
        }
        Dice.prototype._singletonInstance = this;

        console.log("Created Dice");

        this.INTERVAL_SPEED = 50;
        this.DICE_FACE_CSS_CLASSES = ["dOne","dTwo","dThree","dFour","dFive","dSix"];

        this.$container = $(containerSelector);
        this.diceRoledValue = 0;
        this.numberOfRolesToPerform = 0;
        this.roleInterval = null;
        this.diceEndPromise = null;
        this.enabled = true;


        this.clearSingelton = function(){
            Dice.prototype._singletonInstance = null;
        }


        this.roleDice = function(){
            if(this.numberOfRolesToPerform > 0){
                this.diceRoledValue = this.newDiceValue(this.diceRoledValue);
                this.showDiceFace(this.diceRoledValue);
                this.numberOfRolesToPerform--;
            }else{
                this.shaking = false;
                this.stop();
            }
        };

        this.shakeDice = function () {


            if(Math.random() > 0.5) {
                this.$container.effect("shake",{times:2})
            }else{
                this.$container.effect("shake",{times:2,direction:"up"});
            }

        };

        this.start = function(){
            if(this.roleInterval === null && this.enabled === true){
                this.enabled = false;
                this.numberOfRolesToPerform = Math.ceil(Math.random() * 10)+4;
                this.roleInterval = setInterval(function(){ Dice.getInstance().roleDice()},this.INTERVAL_SPEED);
                this.diceEndPromise = {"done":null};
                $("#diceSound").get(0).play();
                return this.diceEndPromise;
            }
        };

        this.stop = function(){
            clearInterval(this.roleInterval);
            this.roleInterval = null;
            this.enabled = true;
            if(this.diceEndPromise.done !== null){
                this.diceEndPromise.done(this.diceRoledValue+1);
            }
        };

        this.newDiceValue = function(old){
            var nextValue = 0;
            do{
                nextValue = Math.floor(Math.random() * 6);
            }while(old == nextValue)
            return nextValue;
        };

        this.showDiceFace = function(index){
            this.$container.attr("class",this.DICE_FACE_CSS_CLASSES[index]);
        } ;

        this.showDiceButton = function(){
           this.$container.show();
        };

        this.hideDiceButton = function(){
            this.$container.hide();
        };

        //init
        this.init = function(){
            this.showDiceFace(0);
        }

        this.init();

    };

    Dice.getInstance = function(containerSelector){
        return new Dice(containerSelector);
    };

    Dice.prototype =  {
        constructor : Dice
    };

    window.Dice = Dice;

})(window,jQuery);