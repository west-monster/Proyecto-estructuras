import { TestBed } from '@angular/core/testing';

import { UndoNoUndoService } from './undo-no-undo.service';

describe('UndoNoUndoService', () => {
  let service: UndoNoUndoService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(UndoNoUndoService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
