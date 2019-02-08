var FlatbondApp = new Vue({
    delimiters: ['[[', ']]'],
    el: '#flatform',
    data: {
        calculatedFee:'',
    },
    computed: {
        getFee: function(){
            getTax = (this.calculatedFee * 20) / 100;
            totalfee = +this.calculatedFee + +getTax;
            return totalfee; 
        }
    },

    methods: {

        submitForm: function(callback) {
                
            var data = new FormData($('#flatbondform')[0]);
            
            FlatBondService.postForm(data, function() {

                
            });

    },


    },
});
