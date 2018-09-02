const request = require('supertest');
var app = require('../../sapient-server.js');

describe('sapient-server', () => {
    describe('TELEMETRIES API v1', () => {
      it('posts a JSON payload', (done) => {
        request(app)
          .post('/telemetries/getTelemetries')
          .expect(200)
          .expect('Content-Type', 'application/json; charset=utf-8')
          .send({measurementUnit: 'C'})
          .end((error) => (error) ? done.fail(error) : done());
      });
    });
  });