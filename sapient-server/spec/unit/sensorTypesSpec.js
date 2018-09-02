const request = require('supertest');
var app = require('../../sapient-server.js');

describe('sapient-server', () => {
  describe('SENSOR-TYPES API v1', () => {
    it('returns a JSON payload', (done) => {
      request(app)
        .get('/sensorTypes/sensorTypes')
        .expect(200)
        .expect('Content-Type', 'application/json; charset=utf-8')
        .end((error) => (error) ? done.fail(error) : done());
    });
  });
});