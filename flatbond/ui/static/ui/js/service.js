var FlatBondService = {
    baseUrl: '/api/',
    csrfToken: '',
    getUrl: function(controller, action) {
        return this.baseUrl + controller + '/' + action;
    },

    ErrorMessage: function (url, jqXHR, textStatus, errorThrown, msg) {   
        msg = "The url: " + url + ". The status = " + jqXHR.status + ". " + jqXHR + " " + textStatus + " " + errorThrown;
            console.log(msg);
    },
    getData: function(url, requestedData, successCallback) {
        $.ajax({
            url: url,
            method: "GET",
            data: requestedData,
            success: function(data) {
                successCallback(data);
            },
            error: function(jqXHR, textStatus, errorThrown) {
                    ErrorMessage(url, jqXHR, textStatus, errorThrown, msg);
                
            }
        });
    }
}
