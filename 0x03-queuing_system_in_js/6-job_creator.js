const kue = require('kue');

const queue = kue.createQueue();

const jobData = {
    phoneNumber: '8166893113',
    message: 'This is a phone number without country code'
};

let queueName = 'push_notification_code';

const job = queue.create(queueName, jobData).save(function(error) {
    if(!error) {
        console.log(`Notification job created: ${job.id}`);
    }
});

job.on('complete', () => {
    console.log('Notification job completed');
});

job.on('failed', () => {
    console.log('Notification job failed');
});
