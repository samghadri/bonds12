var FlatbondApp = new Vue({
    delimiters: ['[[', ']]'],
    el: '#flatform',
    data: {
        // redirectAction: window.location.href = ""
    },
    computed: {},

    methods: {
        submitForm: function(callback) {
                
            var data = new FormData($('#flatbondform')[0]);
            
            FlatBondService.postForm(data, function() {

                
            });

    },


    },
});
