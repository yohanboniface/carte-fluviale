var RevealOSM = L.Control.RevealOSM.extend({

    initialize: function (options) {
        L.Control.RevealOSM.prototype.initialize.call(this, options);
        this.options.excludeKeys = [
            /source/,
            /^ref/,
            /seamark/,
            /^name$/,
            /^harbour$/,
            /^leisure$/,
            /^lock$/,
            /^boat$/,
            /^motorboat$/,
            /^waterway$/,
            /^lock_name$/,
            /^man_made$/,
            /^harbour\:category$/
        ];
        this.options.helpText = "Click on harbours, locks or piers";
        this.options.translateKeys = {
            'harbour:channel': 'VHF',
            'harbour:draft': 'max draft',
            'harbour:length': 'max length'
        };
    },

    getQueryTemplate: function () {
        var template;
        if (this._map.getZoom() < 13) {
            template = '[out:json];node(around:{radius},{lat},{lng})[harbour];out body qt 1;';
        }
        else {
            template = '[out:json];(node(around:{radius},{lat},{lng})[harbour];way(around:{radius},{lat},{lng})[lock];way(around:{radius},{lat},{lng})[man_made=pier]);out body qt 1;';
        }
        return template;
    },

    getRadius: function () {
        return this.options.radius || 300 - (15 * this._map.getZoom());
    },

    formatTitle: function (element) {
        var title,
            className,
            keys = ['lock:name', 'lock_name', 'name'];
        for (var i=0, l=keys.length; i<l; i++) {
            if (element.tags[keys[i]]) {
                title = element.tags[keys[i]];
                break;
            }
        }
        if (!title && element.tags['man_made']) {
            title = element.tags['man_made'];
            className = "pier";
        }
        if (element.tags['harbour'] == 'yes') {
            className = "harbour";
            if (element.tags['seasonal'] == 'yes') {
                className = "seasonal";
            }
        }
        if (title) {
            if (className) { className = ' class="' + className + '"';}
            title = "<h4" + className + ">" + title + "</h4>";
        }
        return title;
    },

    cleanKey: function (element, key) {
        key = L.Control.RevealOSM.prototype.cleanKey.call(this, element, key);
        return key.replace('harbour', '');
    },

    formatIcon: function (element, key) {
        var icon = "";
        if (key.match(/vhf|channel/i)) {
            icon = '<div class="icon vhf info">' + element.tags[key] + "</div>";
        }
        return icon;
    },

    formatPhone: function (element, key) {
        var output = "";
        if (key.match(/phone/i)) {
            output = '<div class="phone">' + element.tags[key] + "</div>";
        }
        return output;
    }

    // formatContent: function (element) {
    //     var content = "",
    //         raw_tags = "",
    //         phone = "",
    //         title = this.formatTitle(element);
    //     if (title) {
    //         content += title;
    //     }
    //     for (var tag in element.tags) {
    //         content += this.formatIcon(element, tag);
    //         phone += this.formatPhone(element, tag);
    //         if (!this.isAllowedKey(tag)) { continue;}
    //         raw_tags += this.formatKey(element, tag);
    //     }
    //     content += phone;
    //     content += '<div class="raw_tags">' + raw_tags + '</div>';
    //     return content;
    // }

});
