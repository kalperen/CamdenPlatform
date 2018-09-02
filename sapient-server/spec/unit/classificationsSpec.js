const request = require('supertest');
var app = require('../../sapient-server.js');

describe('sapient-server', () => {
  describe('CLASSIFICATION API v1', () => {
    it('posts a JSON payload', (done) => {
      request(app)
        .post('/classifications/getClassifications')
        .expect(200)
        .expect('Content-Type', 'application/json; charset=utf-8')
        .send({cameraId: 9})
        .end((error) => (error) ? done.fail(error) : done());
    });
  });
});

