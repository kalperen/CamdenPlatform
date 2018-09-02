const request = require('supertest');
var app = require('../../sapient-server.js');

describe('sapient-server', () => {
  describe('DEVICE API v1', () => {
    it('returns a JSON payload', (done) => {
      request(app)
        .get('/devices/getDevices')
        .expect(200)
        .expect('Content-Type', 'application/json; charset=utf-8')
        .end((error) => (error) ? done.fail(error) : done());
    });
  });
});

describe('sapient-server', () => {
  describe('CAMERA API v1', () => {
    it('posts a JSON payload', (done) => {
      request(app)
        .post('/devices/addDevice')
        .send({deviceId: 5})
        .end((error) => (error) ? done.fail(error) : done());
    });
  });
});

describe('sapient-server', () => {
  describe('CAMERA API v1', () => {
    it('deletes a JSON payload', (done) => {
      request(app)
        .delete('/devices/deleteDevice')
        .send({deviceId: 5})
        .end((error) => (error) ? done.fail(error) : done());
    });
  });
});