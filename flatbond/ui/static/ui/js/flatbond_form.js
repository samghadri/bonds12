var FlatbondFormApp = new Vue({
    delimiters: ['[[', ']]'],
    el: '#flatform',
    data: {
        calculatedFee:'',
        result:{},
        disableSubmit: false,
        hideReset: true,
        monthlyCheck: false
    },
    computed: {
        getFee: function(){
            getTax = (this.calculatedFee * 20) / 100;
            totalfee = +this.calculatedFee + +getTax;
            return totalfee; 
        },
        placeholderText: function() {
            if (!this.monthlyCheck) {
                return 'Minimum amount £25 and Maximum amount £2000';
            }
            if (this.monthlyCheck) {
                return 'Minimum amount £110 and Maximum amount £8660';
            }
        },
    },

    methods: {

    submitForm: function(callback) {
        var data = new FormData($('#flatbondform')[0]);
        var self = this;

        FlatBondService.postForm(data, function(successData) {
            self.result = successData;
            self.disableSubmit = true;
            self.hideReset = false;
        console.log(self.result);

            });
        },
        resetBtn: function(){
            this.disableSubmit = false;
            this.hideReset = true;
        }
    },
});
