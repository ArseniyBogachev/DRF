// import Vue from 'vue'

new Vue({
    el: '#app',
    data: {
        orders: []
    },
    created: function (){
        const vm = this
        axios.get('api/v1/womenlist/')
            .then(function (response) {
                vm.orders = response.data
        })
    }
})