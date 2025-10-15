
#%%imports
import pytest
import datetime
import time
from cn5_pkg import cn5


#%%tests
class Test_runtime_estimate:
    
    @pytest.fixture(
        params=[
            (lambda x: time.sleep(0.1), [1], 1, 10, "test1", datetime.timedelta(seconds=0.1), datetime.timedelta(seconds=0.1*10)),
        ]
    )
    def action(self, request):
        #arrange

        #act
        f, args, nreps, nest, prefix, rt_mean_true, rt_est_true = request.param
        rt_mean, rt_est = cn5.runtime_estimate(f, *args, nreps=nreps, nest=nest, prefix=prefix)

        return rt_mean, rt_est, rt_mean_true, rt_est_true

    #assert
    def test_outtypes(self, action):
        rt_mean, rt_est, _, _ = action
        assert isinstance(rt_mean, datetime.timedelta)
        assert isinstance(rt_est, datetime.timedelta)

    def test_intypes(self):
        with pytest.raises(TypeError):
            cn5.runtime_estimate(None, [1], nreps=1, nest=10, prefix=None)
            cn5.runtime_estimate(lambda x: time.sleep(0.1), [1], nreps=1.0, nest=10, prefix=None)
            cn5.runtime_estimate(lambda x: time.sleep(0.1), [1], nreps=1, nest=10.0, prefix=None)
            cn5.runtime_estimate(lambda x: time.sleep(0.1), [1], nreps=1, nest=10.0, prefix=1)

    def test_output(self, action):
        rt_mean, rt_est, rt_mean_true, rt_est_true = action
        assert rt_mean.total_seconds() == pytest.approx(rt_mean_true.total_seconds(), rel=1e-2)
        assert rt_est.total_seconds() == pytest.approx(rt_est_true.total_seconds(), rel=1e-2)
