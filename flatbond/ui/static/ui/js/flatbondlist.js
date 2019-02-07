var FlatbondApp = new Vue({
    delimiters: ['[[', ']]'],
    el: '#flatbondid',
    data: {
        flatbond: {}
    },
    computed: {},
    created: function() {
        this.getflatbond();
    },
    methods: {
        GetId: function () {
            var endpart = location.pathname.split("/").filter(Boolean);
            return endpart[endpart.length - 1];
        },
        getflatbond: function() {
            var footerId = this.GetId();
            var data = {
                "csrfmiddlewaretoken": FlatBondService.csrfToken
            }
            FlatBondService.getData(FlatBondService.getUrl('flatbond', footerId), data,
                function(callbackResult) {
                    FlatbondApp.flatbond = callbackResult;
                });
        },
    },
});
