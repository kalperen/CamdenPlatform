const request = require('supertest');
var app = require('../../sapient-server.js');

describe('sapient-server', () => {
  describe('CAMERA API v1', () => {
    it('returns a JSON payload', (done) => {
      request(app)
        .get('/cameras/getCameras')
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
        .post('/cameras/addCamera')
        .send({cameraId: 9})
        .end((error) => (error) ? done.fail(error) : done());
    });
  });
});

describe('sapient-server', () => {
  describe('CAMERA API v1', () => {
    it('deletes a JSON payload', (done) => {
      request(app)
        .delete('/cameras/deleteCamera')
        .send({cameraId: 9})
        .end((error) => (error) ? done.fail(error) : done());
    });
  });
});