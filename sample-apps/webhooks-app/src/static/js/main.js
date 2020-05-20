function requestNotShownEventsCount() {
    return new Promise((resolve) => {
        $.getJSON("/events/updates?after=" + $('#updates-alert').attr('data-now') , data => {
            const { updatesCount } = data;
            resolve(updatesCount);
        });
    });
}

async function displayNotShownEventsAlertIfNeed() {
    const updatesCount = await requestNotShownEventsCount();
    if (updatesCount > 0) {
        $('#empty-message').hide();
        $('#updates-alert').show();
    }
}

$(document).ready(async () => {
    setInterval(displayNotShownEventsAlertIfNeed, 10000);
});
